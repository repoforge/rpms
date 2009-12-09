# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

### RHEL ships with perl-URI already
# ExclusiveDist: none

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI

Summary: Perl module that implements Uniform Resource Identifiers (absolute and relative)
Name: perl-URI
Version: 1.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI/

Source: http://www.cpan.org/modules/by-module/URI/URI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(MIME::Base64) >= 2


%description
perl-URI is a Perl module that implements Uniform Resource Identifiers.
(absolute and relative)

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
%doc %{_mandir}/man3/URI.3pm*
%doc %{_mandir}/man3/URI::*.3pm*
%{perl_vendorlib}/URI/
%{perl_vendorlib}/URI.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.51-1
- Updated to version 1.51.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.38-1
- Updated to version 1.38.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.35-1
- Initial package. (using DAR)
