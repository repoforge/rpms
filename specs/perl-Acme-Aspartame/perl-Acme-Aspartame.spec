# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Aspartame

Summary: raise the alarum if a source filter was used
Name: perl-Acme-Aspartame
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Aspartame/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Aspartame-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Bloom::Filter)
BuildRequires: perl(Filter::Simple)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Switch)
BuildRequires: perl(Test::More)

%description
raise the alarum if a source filter was used.

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
%doc %{_mandir}/man3/Acme::Aspartame.3pm*
%dir %{perl_vendorlib}/Acme/
#%{perl_vendorlib}/Acme/Aspartame/
%{perl_vendorlib}/Acme/Aspartame.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
