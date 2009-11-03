# $Id$
# Authority: dag
# Upstream: Shannon Eric Peevey <speeves$erikin,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-AuthenNIS

Summary: mod_perl NIS Authentication module
Name: perl-Apache-AuthenNIS
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-AuthenNIS/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-AuthenNIS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(ExtUtils::AutoInstall) >= 0.52
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Storable)

%description
mod_perl NIS Authentication module.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" NAME="Apache::uthenNIS"
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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Apache::AuthenNIS.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/AuthenNIS.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
