# $Id$
# Authority: dries
# Upstream: Taisuke Yamada <tyamadajp$list,rakugaki,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-SimpleTemplate

Summary: Yet another module for template processing
Name: perl-Text-SimpleTemplate
Version: 0.36
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-SimpleTemplate/

Source: http://www.cpan.org/modules/by-module/Text/Text-SimpleTemplate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is yet another library for template-based text generation.

Template-based text generation is a way to separate program code and
data, so non-programmer can control final result (like HTML) as desired
without tweaking the program code itself. By doing so, jobs like website
maintenance is much easier because you can leave program code unchanged
even if page redesign was needed.

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
%doc README.TXT
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/SimpleTemplate.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Initial package.
