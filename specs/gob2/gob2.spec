# $Id$
# Authority: dag

##ExcludeDist: fc2

Summary: The GTK+ Object Builder, a preprocessor for making GObjects with inline C code
Name: gob2
Version: 2.0.9
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.5z.com/jirka/gob.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.5z.com/pub/gob/gob2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.0

%description
GOB is a simple preprocessor for making GTK+ objects.  It makes objects from a
single file which has inline C code so that you don't have to edit the
generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%doc -P examples/[^M]*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/aclocal/*

%changelog
* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 2.0.9-1
- Updated to release 2.0.9.

* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 2.0.8-1
- Updated to release 2.0.8.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 2.0.5-0
- Initial package. (using DAR)
