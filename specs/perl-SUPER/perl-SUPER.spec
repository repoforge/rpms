# $Id$
# Authority: dag
# Upstream: Created by Simon Cozens, C<simon$cpan,org>,

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SUPER

Summary: Control superclass method dispatch
Name: perl-SUPER
Version: 1.16
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SUPER/

Source: http://www.cpan.org/modules/by-module/SUPER/SUPER-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(Test::Simple) >= 0.61

%description
Control superclass method dispatch.

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
%doc %{_mandir}/man3/SUPER.3pm*
%{perl_vendorlib}/SUPER.pm

%changelog
* Sun Aug 02 2009 Christoph Maser <cmr@financial.com> - 1.16-2
- Comment out BuildRequires so build on el4 works.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
