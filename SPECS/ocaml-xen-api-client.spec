%global package_speccommit 37aa7dfdb8bb6a5bbb1feadafdabc7b8d5a4c92b
%global package_srccommit v1.9.0
%define debug_package %{nil}

Name:           ocaml-xen-api-client
Version: 1.9.0
Release: 20.1%{?xsrel}%{?dist}
Summary:        Ocaml bindings to the Xapi API
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/xapi-project/xen-api-client/

Source0: xen-api-client-1.9.0.tar.gz

BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  xapi-client-devel
Requires:       ocaml

%description
OCaml bindings to the Xapi API, include support for concurrent
client using the lwt and async libraries.

%package        devel
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
* Thu Oct 24 2024 Gael Duperrey <gduperrey@vates.tech> - 1.9.0-20.1
- Rebuild after sync with hotfix XS82ECU1074
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Thu Aug 29 2024 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-20
- - Bump release and rebuild
- * Wed Jun 19 2024 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-19
- - Bump release and rebuild

* Tue Jun 04 2024 Gael Duperrey <gduperrey@vates.tech> - 1.9.0-18.1
- Rebuild after sync with hotfix XS82ECU1064
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Fri Mar 08 2024 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-18
- - Bump release and rebuild
- * Wed Mar 06 2024 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-17
- - Bump release and rebuild
- * Tue Mar 05 2024 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-16
- - Bump release and rebuild
- * Fri Nov 03 2023 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-15
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-14
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-13
- - Bump release and rebuild
- * Wed Oct 18 2023 Christian Lindig <christian.lindig@cloud.com> - 1.9.0-12
- - Bump release and rebuild

* Fri Oct 13 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-11.1
- Rebuild after sync with hotfix XS82ECU1049
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Mon Oct 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.9.0-11
- - Bump release and rebuild

* Wed Aug 09 2023 Gael Duperrey <gduperrey@vates.fr> - 1.9.0-10.1
- Sync with hotfix XS82ECU1040
- *** Upstream changelog ***
- * Thu Jul 20 2023 Rob Hoes <rob.hoes@citrix.com> - 1.9.0-10
- - Bump release and rebuild
- * Mon Jun 19 2023 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-9
- - Bump release and rebuild
- * Thu Jun 08 2023 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-8
- - Bump release and rebuild
- * Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-7
- - Bump release and rebuild
- * Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-6
- - Bump release and rebuild

* Fri Apr 14 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-5.1
- Sync with hotfix XS82ECU1027
- *** Upstream changelog ***
- * Tue Feb 28 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.9.0-5
- - Change license to be a valid SPDX identifier
- - Fix xen BuildReqs
- - Remove macro for dependency generator
- * Mon Feb 20 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.9.0-4
- - Bump to avoid conflict with existing version tag in repo

* Wed Aug 17 2022 Gael Duperrey <gduperrey@vates.fr> - 1.9.0-3.1
- Rebuild for updated varstored-guard and xcp-networkd from XS82ECU1011

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.9.0-3
- Bump package after xs-opam update

* Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.9.0-2
- bump packages after xs-opam update

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

