# $Id$

# Authority: dag
# Upstream: <gtk-perl-list@gnome.org>

%define real_name Gnome2

Summary: Perl interface to the 2.x series of the GNOME libraries
Name: perl-Gnome2
Version: 1.00
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/Gtk2-Perl/Gnome2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig),
BuildRequires: perl(Glib), perl(Gtk2), perl(Gnome2::VFS)
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
%doc AUTHORS ChangeLog LICENSE MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
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
