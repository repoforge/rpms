# $Id$
# Authority: dag
# Upstream: Diab Jerius <djerius$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Expect-Simple

Summary: Wrapper around the Expect module
Name: perl-Expect-Simple
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Expect-Simple/

Source: http://www.cpan.org/modules/by-module/Expect/Expect-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Expect)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Expect::Simple is a wrapper around the Expect module which should
suffice for simple applications. It hides most of the Expect
machinery; the Expect object is available for tweaking if need be.

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
%doc ChangeLog Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Expect::Simple.3pm*
%dir %{perl_vendorlib}/Expect/
#%{perl_vendorlib}/Expect/Simple/
%{perl_vendorlib}/Expect/Simple.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
