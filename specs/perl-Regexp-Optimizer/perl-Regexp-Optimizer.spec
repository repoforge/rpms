# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Optimizer

Summary: Perl module to build regular expressions out of a list of words
Name: perl-Regexp-Optimizer
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Optimizer/

Source: http://www.cpan.org/modules/by-module/Regexp/Regexp-Optimizer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Regexp-Optimizer is a Perl module to build regular expressions
out of a list of words.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Regexp::List.3pm*
%doc %{_mandir}/man3/Regexp::Optimizer.3pm*
%dir %{perl_vendorlib}/Regexp/
%{perl_vendorlib}/Regexp/List.pm
%{perl_vendorlib}/Regexp/Optimizer.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
