# $Id$

# Authority: dag
# Upstream: <gtk-perl-list$gnome,org>

%define real_name Gnome2

Summary: Perl interface to the 2.x series of the GNOME libraries
Name: perl-Gnome2
Version: 1.041
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2/

Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSCH/Gnome2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig),
BuildRequires: perl(Glib), perl(Gtk2), perl(Gnome2::VFS), perl(Gnome2::Canvas)
BuildRequires: libgnomeui-devel >= 2.0.0
Requires: perl >= 0:5.8.0

%description
Perl bindings to the 2.x series of the Gnome widget set.  This module allows
you to write graphical user interfaces in a perlish and object-oriented way,
freeing you from the casting and memory management in C, yet remaining very
close in spirit to original API.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.041-1
- Updated to release 1.041.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.040-1
Updated to release 1.040.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.023-1.2
- Rebuild for Fedora Core 5.

* Sat Oct 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.023-1
- Updated to release 1.023.

* Tue Mar 30 2004 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 0.38-0
- Updated to release 0.38.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.34-0
- Updated to release 0.34.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.30-0
- Updated to release 0.30.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.28-0
- Initial package. (using DAR)
