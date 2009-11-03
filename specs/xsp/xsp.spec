# $Id$
# Authority: dag

Summary: Small web server that hosts ASP.NET
Name: xsp
Version: 1.0.5
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.go-mono.com/

Source: http://www.go-mono.com/archive/%{version}/xsp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-core, mono-data, mono-web

%description
The XSP server is a small web server that hosts the Mono System.Web
classes for running what is commonly known as ASP.NET.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\@prefix\@/share/doc|\$(docdir)|g;
		s|\@prefix\@/bin|\$(bindir)|g;
		s|\$\(LOCAL_LIB_DIR\)|\$(libdir)|g;
	' Makefile.in */Makefile.in */*/Makefile.in */*/*/Makefile.in */*/*/*/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	docdir="../rpm-doc"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_includedir}/X11/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README rpm-doc/*
#%doc %{_mandir}/man1/asp_state.1*
#%doc %{_mandir}/man1/dbsessmgr.1*
%doc %{_mandir}/man1/mod-mono-server.1*
%doc %{_mandir}/man1/xsp.1*
#%{_bindir}/asp_state.exe*
#%{_bindir}/dbsessmgr.exe*
%{_bindir}/mod-mono-server*
%{_bindir}/xsp*
%{_libdir}/*.dll

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.
- Updated to release 1.0.4.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Initial package. (using DAR)
