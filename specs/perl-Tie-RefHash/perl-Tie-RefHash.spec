# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-RefHash

Summary: Use references as hash keys
Name: perl-Tie-RefHash
Version: 1.37
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-RefHash/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-RefHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Use references as hash keys.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Tie::RefHash.3pm*
%dir %{perl_vendorlib}/Tie/
#%{perl_vendorlib}/Tie/RefHash/
%{perl_vendorlib}/Tie/RefHash.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 1.37-1
- Initial package. (using DAR)
