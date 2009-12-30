# $Id$
# Authority: dag
# Upstream: David Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Capture-Tiny

Summary: Capture STDOUT and STDERR from Perl, XS or external programs
Name: perl-Capture-Tiny
Version: 0.06
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Capture-Tiny/

#Source: http://www.cpan.org/modules/by-module/Capture/Capture-Tiny-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.006

%description
Capture STDOUT and STDERR from Perl, XS or external programs.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo examples/
%doc %{_mandir}/man3/Capture::Tiny.3pm*
%dir %{perl_vendorlib}/Capture/
#%{perl_vendorlib}/Capture/Tiny/
%{perl_vendorlib}/Capture/Tiny.pm
%{perl_vendorlib}/Capture/Tiny.pod

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.06-2
- Remove version number for Test::More requirement

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
