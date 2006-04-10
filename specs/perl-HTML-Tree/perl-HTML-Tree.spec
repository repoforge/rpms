# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tree

Summary: HTML-Tree module for perl
Name: perl-HTML-Tree
Version: 3.18
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tree/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Tree-%{version}.tar.gz
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
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/HTML-Tree/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/HTML/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.18-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 3.18-0
- Updated to release 3.18.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 3.17-0
- Initial package. (using DAR)
