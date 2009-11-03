# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-IMAPUtf7

Summary: Perl module to deal with IMAP UTF7
Name: perl-Unicode-IMAPUtf7
Version: 2.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-IMAPUtf7/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-IMAPUtf7-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-IMAPUtf7 is a Perl module to deal with IMAP UTF7.

This package contains the following Perl module:

    Unicode::IMAPUtf7

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
%doc %{_mandir}/man3/Unicode::IMAPUtf7.3pm*
%dir %{perl_vendorlib}/Unicode/
#%{perl_vendorlib}/Unicode/IMAPUtf7/
%{perl_vendorlib}/Unicode/IMAPUtf7.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 2.00-1
- Initial package. (using DAR)
