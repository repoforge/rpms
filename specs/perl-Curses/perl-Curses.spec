# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Curses

Summary: Perl module for terminal screen handling and optimization
Name: perl-Curses
Version: 1.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Curses/

Source: http://www.cpan.org/modules/by-module/Curses/Curses-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, ncurses-devel
Requires: perl

%description
Perl module for terminal screen handling and optimization

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|Perl_(sv_isa\(sv, "Curses::Window"\))|$1|' Curses.c

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic Copying INSTALL MANIFEST README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Curses.pm
%{perl_vendorarch}/auto/Curses/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
