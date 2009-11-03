# $Id$
# Authority: dag

Summary: GOB, The GTK+ Object Builder
Name: gob
Version: 1.0.12
Release: 0.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.5z.com/jirka/gob.html

Source: http://ftp.5z.com/pub/gob/gob-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, glib2-devel, glib-devel
BuildRequires: autoconf, automake

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
%doc -P examples/[^M]*
%doc %{_mandir}/man1/gob.1*
%{_bindir}/gob
%{_datadir}/aclocal/gob.m4

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.12-0.2
- Rebuild for Fedora Core 5.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.0.12
- Initial package. (using DAR)
