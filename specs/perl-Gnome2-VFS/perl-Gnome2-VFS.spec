# $Id$

# Authority: dag
# Upstream: <gtk-perl-list$gnome,org>

%define real_name Gnome2-VFS

Summary: Perl interface to the 2.x series of the GNOME VFS library
Name: perl-Gnome2-VFS
Version: 1.041
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://gtk2-perl.sourceforge.net/

#Source: http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/Gtk2-Perl/Gnome2-VFS-%{version}.tar.gz
Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-VFS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig),
BuildRequires: perl(Glib), perl(Gtk2)
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST* README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.041-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.041-1
- Updated to release 1.041.

* Tue Mar 30 2004 Dag Wieers <dag@wieers.com> - 1.001-1
- Updated to release 1.001.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
