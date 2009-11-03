# $Id$
# Authority: dag
# Upstream: John Kirk <johnkirk$dystanhays,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qtk-QuickTk
%define real_version 0.9

Summary: Perl module named Qtk-QuickTk
Name: perl-Qtk-QuickTk
Version: 0.90
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qtk-QuickTk/

Source: http://www.cpan.org/authors/id/J/JN/JNK/Qtk-QuickTk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qtk-QuickTk is a Perl module.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc %{_mandir}/man3/Qtk::*.3pm*
%dir %{perl_vendorlib}/auto/Qtk/
%{perl_vendorlib}/auto/Qtk/QuickTk/
%dir %{perl_vendorlib}/Qtk/
%{perl_vendorlib}/Qtk/QuickTk/
%{perl_vendorlib}/Qtk/QuickTk.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.90-1
- Switch to upstream version.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Initial package. (using DAR)
