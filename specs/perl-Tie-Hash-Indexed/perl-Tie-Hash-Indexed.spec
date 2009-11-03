# $Id$
# Authority: dag
# Upstream: Marcus Holland-Moritz <mhx$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Hash-Indexed

Summary: Ordered hashes for Perl
Name: perl-Tie-Hash-Indexed
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Hash-Indexed/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Hash-Indexed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Ordered hashes for Perl.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Tie::Hash::Indexed.3pm*
%dir %{perl_vendorarch}/auto/Tie/
%dir %{perl_vendorarch}/auto/Tie/Hash/
%{perl_vendorarch}/auto/Tie/Hash/Indexed/
%dir %{perl_vendorarch}/Tie/
%dir %{perl_vendorarch}/Tie/Hash/
%{perl_vendorarch}/Tie/Hash/Indexed.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
