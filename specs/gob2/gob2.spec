# $Id$
# Authority: dag

##ExcludeDist: fc2

Summary: The GTK+ Object Builder, a preprocessor for making GObjects with inline C code
Name: gob2
Version: 2.0.14
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.5z.com/jirka/gob.html

Source: http://ftp.5z.com/pub/gob/gob2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### gob2 2.0.9 was the last one to generate glib 2.2 compatible code
BuildRequires: glib2-devel >= 2.4.0, flex, bison

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
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS README TODO
%doc examples/*.gob
%doc %{_mandir}/man1/gob2.1*
%{_bindir}/gob2
%{_datadir}/aclocal/gob2.m4

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.14-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 06 2006 Dag Wieers <dag@wieers.com> - 2.0.14-1
- Updated to release 2.0.14.

* Sun Jul 24 2005 Dag Wieers <dag@wieers.com> - 2.0.12-1
- Updated to release 2.0.12.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 2.0.11-1
- Updated to release 2.0.11.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 2.0.10-1
- Updated to release 2.0.10.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 2.0.9-1
- Updated to release 2.0.9.

* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 2.0.8-1
- Updated to release 2.0.8.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 2.0.5-0
- Initial package. (using DAR)
