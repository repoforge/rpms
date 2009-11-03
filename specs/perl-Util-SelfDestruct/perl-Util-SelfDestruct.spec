# $Id$
# Authority: dag
# Upstream: Nicola Worthington <nicolaw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Util-SelfDestruct

Summary: Perl module to conditionally prevent execution of a script
Name: perl-Util-SelfDestruct
Version: 1.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Util-SelfDestruct/

Source: http://www.cpan.org/authors/id/N/NI/NICOLAW/Util-SelfDestruct-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
Conditionally prevent execution of a script.
perl-Util-SelfDestruct is a Perl module to conditionally prevent
execution of a script.

This package contains the following Perl module:

    Util::SelfDestruct

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
%doc Changes INSTALL LICENSE MANIFEST META.yml NOTICE README
%doc %{_mandir}/man3/Util::SelfDestruct.3pm*
%dir %{perl_vendorlib}/Util/
#%{perl_vendorlib}/Util/SelfDestruct/
%{perl_vendorlib}/Util/SelfDestruct.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Initial package. (using DAR)
