# $Id$
# Authority: dries
# Upstream: Rob Casey <rob,casey$bluebottle,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Upload

Summary: CGI class for handling browser file uploads
Name: perl-CGI-Upload
Version: 1.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Upload/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Upload-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module has been written to provide a simple and secure manner by
which to handle files uploaded in multipart/form-data requests through a
web browser. The primary advantage which this module offers over
existing modules is the single interface which it provides for the most
often required information regarding files uploaded in this manner.

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
%doc %{_mandir}/man3/CGI::Upload.3pm*
%dir %{perl_vendorlib}/CGI/
#%{perl_vendorlib}/CGI/Upload/
%{perl_vendorlib}/CGI/Upload.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
