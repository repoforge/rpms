# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net_SSLeay.pm

Summary: Net-SSLeay module for perl
Name: perl-Net-SSLeay
Version: 1.25
Release: 2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSLeay.pm/

Source: http://www.cpan.org/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-SSLeay module for perl.

%prep
%setup -n %{real_name}-%{version} 

%{__perl} -pi -e 's|^\s*#!/.*bin/perl|#!%{__perl}|;' SSLeay.pm examples/*.pl

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL %{_prefix} INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes Credits MANIFEST QuickRef README examples/
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/ptrtstrun.pl
%{perl_vendorarch}/Net/SSLeay/
%{perl_vendorarch}/Net/SSLeay.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/SSLeay/

%changelog
* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 1.25-2
- Cosmetic cleanup.

* Fri Nov 12 2004 Dries Verachtert <dries@ulyssis.org> 1.25-1
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> 1.25-0
- Update to release 1.25.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.23-0
- Initial package. (using DAR)
