# $Id$

# Authority: atrpms

%define real_name HTML-Tree

Summary: HTML-Tree module for perl
Name: perl-HTML-Tree
Version: 3.18
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tree/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/HTML-Tree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
HTML-Tree module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 3.18-0
- Updated to release 3.18.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 3.17-0
- Initial package. (using DAR)
