# $Id$
# Authority: cmr
# Upstream: Trevor Hall <wazzuteke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Clone-Fast

Summary: Perl module named Clone-Fast
Name: perl-Clone-Fast
Version: 0.93
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Clone-Fast/

Source: http://www.cpan.org/modules/by-module/Clone/Clone-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Clone-Fast is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Clone::Fast.3pm*
%dir %{perl_vendorarch}/auto/Clone/
%{perl_vendorarch}/auto/Clone/Fast/
%dir %{perl_vendorarch}/Clone/
%{perl_vendorarch}/Clone/Fast.pm

%changelog
* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 0.93-1
- Initial package. (using DAR)
