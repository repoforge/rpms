# $Id$

# Authority: dag

Summary: Small web server that hosts ASP.NET.
Name: xsp
Version: 0.9
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://www.go-mono.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.go-mono.org/archive/xsp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mono-devel

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
	docdir="../doc-rpm"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_includedir}/X11/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README doc-rpm/*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.dll

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Initial package. (using DAR)
