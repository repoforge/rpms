# $Id$
# Authority: dries
# Upstream: Steven McDougall <swmcd$world,std,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name News-Newsrc

Summary: Manage newsrc files
Name: perl-News-Newsrc
Version: 1.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/News-Newsrc/

Source: http://www.cpan.org/modules/by-module/News/News-Newsrc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
News::Newsrc manages newsrc files.

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
%doc Changes MANIFEST META.yml Newsrc.pm README
%doc %{_mandir}/man3/News::Newsrc.3pm*
%dir %{perl_vendorlib}/News/
#%{perl_vendorlib}/News/Newsrc/
%{perl_vendorlib}/News/Newsrc.pm

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
