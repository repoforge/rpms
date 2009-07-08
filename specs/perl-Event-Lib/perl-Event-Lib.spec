# $Id$
# Authority: cmr
# Upstream: Tassilo von Parseval <tassilo,von,parseval$rwth-aachen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event-Lib

Summary: Perl module named Event-Lib
Name: perl-Event-Lib
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Event-Lib/

Source: http://www.cpan.org/modules/by-module/Event/Event-Lib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel
BuildRequires: perl
Requires: libevent

%description
perl-Event-Lib is a Perl module.

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
%doc %{_mandir}/man3/Event::Lib.3pm*
%dir %{perl_vendorarch}/auto/Event/
%{perl_vendorarch}/auto/Event/Lib/
%dir %{perl_vendorarch}/Event/
%{perl_vendorarch}/Event/Lib.pm

%changelog
* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Initial package. (using DAR)
