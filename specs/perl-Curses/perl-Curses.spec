# $Id: perl-Curses.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag

%define real_name Curses

Summary: Perl module for terminal screen handling and optimization
Name: perl-Curses
Version: 1.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Curses/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/W/WP/WPS/Curses-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, ncurses-devel
Requires: perl

%description
Perl module for terminal screen handling and optimization

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|Perl_(sv_isa\(sv, "Curses::Window"\))|$1|' Curses.c

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
%doc Artistic Copying INSTALL MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
