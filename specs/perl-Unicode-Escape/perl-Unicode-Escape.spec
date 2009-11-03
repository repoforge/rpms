# $Id$
# Authority: dag
# Upstream: Hitoshi Amano <seijro$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Escape
%define real_version 0.000002

Summary: Perl module that implements escape and unescape Unicode characters other than ASCII
Name: perl-Unicode-Escape
Version: 0.0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Escape/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Escape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-Escape is a Perl module that implements escape and unescape
Unicode characters other than ASCII.

This package contains the following Perl module:

    Unicode::Escape

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unicode::Escape.3pm*
%dir %{perl_vendorlib}/Unicode/
#%{perl_vendorlib}/Unicode/Escape/
%{perl_vendorlib}/Unicode/Escape.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.0.2-1
- Initial package. (using DAR)
