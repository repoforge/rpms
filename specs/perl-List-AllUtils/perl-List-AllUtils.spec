# $Id$
# Authority: shuff
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-AllUtils

Summary: Combines List::Util and List::MoreUtils in one bite-sized package
Name: perl-%{real_name}
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-AllUtils/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/List-AllUtils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils) >= 0.22
BuildRequires: perl(List::Util) >= 1.19
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.0
Requires: perl(List::MoreUtils) >= 0.22
Requires: perl(List::Util) >= 1.19

%description
Are you sick of trying to remember whether a particular helper is defined in
List::Util or List::MoreUtils? I sure am. Now you don't have to remember. This
module will export all of the functions that either of those two modules
defines.


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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/List/
%{perl_vendorlib}/List/*

%changelog
* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial package.
