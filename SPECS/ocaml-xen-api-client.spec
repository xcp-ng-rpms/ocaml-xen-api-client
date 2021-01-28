%define debug_package %{nil}

Name:           ocaml-xen-api-client
Version:        1.9.0
Release:        1%{?dist}
Summary:        Ocaml bindings to the Xapi API
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xen-api-client/


Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-client/archive?at=v1.9.0&format=tar.gz&prefix=ocaml-xen-api-client-1.9.0#/xen-api-client-1.9.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-client/archive?at=v1.9.0&format=tar.gz&prefix=ocaml-xen-api-client-1.9.0#/xen-api-client-1.9.0.tar.gz) = 63357e49b89dcfdca9839823ce6588e4501697d2

Patch1000: xen-api-client-1.9.0-handle-ipv6.patch

BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xapi-client-devel
Requires:       ocaml

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
OCaml bindings to the Xapi API, include support for concurrent
client using the lwt and async libraries.

%package        devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-client/archive?at=v1.9.0&format=tar.gz&prefix=ocaml-xen-api-client-1.9.0#/xen-api-client-1.9.0.tar.gz) = 63357e49b89dcfdca9839823ce6588e4501697d2
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xs-opam-repo
Requires:       xapi-client-devel
Requires:       xen-dom0-libs-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1

%build
make

%check
make test

%install
make DESTDIR=%{buildroot} install

%files
%{ocaml_libdir}/xen-api-client/META
%{ocaml_libdir}/xen-api-client/*.cma
%{ocaml_libdir}/xen-api-client/*.cmi
%{ocaml_libdir}/xen-api-client-lwt/META
%{ocaml_libdir}/xen-api-client-lwt/*.cma
%{ocaml_libdir}/xen-api-client-lwt/*.cmi
%{ocaml_libdir}/xen-api-client-async/META
%{ocaml_libdir}/xen-api-client-async/*.cma
%{ocaml_libdir}/xen-api-client-async/*.cmi
%{ocaml_libdir}/xen-api-client*/dune-package

%files devel
%{ocaml_docdir}/xen-api-client
%exclude %{ocaml_libdir}/xen-api-client/*.cmt
%exclude %{ocaml_libdir}/xen-api-client/*.cmti
%exclude %{ocaml_libdir}/xen-api-client/opam
%{ocaml_libdir}/xen-api-client/*.a
%{ocaml_libdir}/xen-api-client/*.cmxa
%{ocaml_libdir}/xen-api-client/*.cmxs
%{ocaml_libdir}/xen-api-client/*.cmx
%{ocaml_libdir}/xen-api-client/*.ml*
%exclude %{ocaml_libdir}/xen-api-client-lwt/*.cmt
%exclude %{ocaml_libdir}/xen-api-client-lwt/*.cmti
%exclude %{ocaml_libdir}/xen-api-client-lwt/opam
%exclude %{ocaml_docdir}/xen-api-client-lwt/*
%{ocaml_libdir}/xen-api-client-lwt/*.a
%{ocaml_libdir}/xen-api-client-lwt/*.cmxa
%{ocaml_libdir}/xen-api-client-lwt/*.cmxs
%{ocaml_libdir}/xen-api-client-lwt/*.cmx
%{ocaml_libdir}/xen-api-client-lwt/*.ml*
%exclude %{ocaml_libdir}/xen-api-client-async/*.cmt
%exclude %{ocaml_libdir}/xen-api-client-async/*.cmti
%exclude %{ocaml_libdir}/xen-api-client-async/opam
%exclude %{ocaml_docdir}/xen-api-client-async/*
%{ocaml_libdir}/xen-api-client-async/*.a
%{ocaml_libdir}/xen-api-client-async/*.cmxa
%{ocaml_libdir}/xen-api-client-async/*.cmxs
%{ocaml_libdir}/xen-api-client-async/*.cmx
%{ocaml_libdir}/xen-api-client-async/*.ml*

%changelog
* Mon May 04 2020 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-1
- maintenance: update opam dependencies

* Wed Feb 12 2020 Christian Lindig <christian.lindig@citrix.com> - 1.8.0-1
- CP-32846 drop legacy ssl support
- maintenance: fix travis build

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.7.0-3
- bump packages after xs-opam update

* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-1
- Prepare for Dune 1.6

* Thu Jan 17 2019 Christian Lindig <christian.lindig@citrix.com> - 1.6.0-1
- Corrected coverage rewriter.

* Fri Jan 11 2019 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- Use xapi-rrd; rrd is being deprecated.
- Moved from jbuilder to dune.
- Updated opam files.

* Tue Sep 18 2018 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- Move to dune and fix opam dependencies
- Update .travis.yml to pin all opam packages in this repo, use OCaml 4.06

* Tue May 29 2018 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- async: make safe-string compliant
- lwt: make safe-string compliant
- lwt_examples: fix use of cohttp (>= 1.0.0)

* Thu May 24 2018 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- CA-289145: close socket if error occurs when using lwt connect
- xen_api_metrics: fix deprecation warning
- async_examples/event_test: update code for more recent version of core/base

* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Fri Jan 26 2018 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- lwt/jbuild: update dependencies to Lwt 3
- Update to be compliant with async 0.10.0.
- Update to be compliant with core 0.10.0.
- xen-api-client-lwt: add missing lwt_ssl
- Makefile: fix install locations

* Fri Dec 08 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-1
- Initial package

