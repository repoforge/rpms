# $Id$
# Authority: dag
# Upstream: Yasuhiro Horiuchi <yasuhiro$hori-uchi,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Lite-TT

Summary: TT enabled MIME::Lite wrapper
Name: perl-MIME-Lite-TT
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Lite-TT/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Lite-TT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
TT enabled MIME::Lite wrapper.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/MIME::Lite::TT.3pm*
%dir %{perl_vendorlib}/MIME/
%dir %{perl_vendorlib}/MIME/Lite/
#%{perl_vendorlib}/MIME/Lite/TT/
%{perl_vendorlib}/MIME/Lite/TT.pm

%changelog
* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
