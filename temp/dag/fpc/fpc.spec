# Authority: dag

Summary: Free Pascal Compiler.
Name: fpc
Version: 1.0.6
Release: 0
License: GPL
Group: Development/Languages
URL: http://www.freepascal.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: fpc-1.0.6-src.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: fpc
ExclusiveArch: i386 i586 i686

%description	
The Free Pascal Compiler is a Turbo Pascal 7.0 and Delphi compatible 32bit
Pascal Compiler. It comes with fully TP 7.0 compatible run-time library.
Some extensions are added to the language, like function overloading. Shared
libraries can be linked. Basic Delphi support is already implemented (classes,
exceptions,ansistrings,RTTI). This package contains commandline compiler and
utils. Provided units are the runtime library (RTL), free component library
(FCL), gtk,ncurses,zlib, mysql,postgres,ibase bindings.

%prep
%setup -c

%build
make compiler_cycle FPC_VERSION="$(ppc386 -iV)"
make rtl_clean rtl_smart packages_base_smart fcl_smart packages_extra_smart utils_all \
	FPC="%{_builddir}%{_buildsubdir}/compiler/ppc386"

%install
%{__rm} -rf %{buildroot}
make compiler_distinstall rtl_distinstall packages_distinstall fcl_distinstall utils_distinstall demo_install doc_install man_install \
	FPC="%{_builddir}%{_buildsubdir}/compiler/ppc386" \
	INSTALL_PREFIX="%{buildroot}/usr" \
	INSTALL_DOCDIR="%{buildroot}%{_docdir}/fpc" \
	INSTALL_SOURCEDIR="%{buildroot}%{_docdir}/fpc"

%{_ln_s} -f %{_libdir}/fpc/%{version}/ppc386 %{buildroot}%{_bindir}/ppc386
%{buildroot}%{_libdir}/fpc/%{version}/samplecfg %{_libdir}/fpc/%{version}
	
%clean
%{__rm} -rf %{buildroot}
	
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_libdir}/fpc/

%changelog
* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
