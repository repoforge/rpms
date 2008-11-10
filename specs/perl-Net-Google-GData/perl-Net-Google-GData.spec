# $Id$
# Authority: dag
# Upstream: Alan Young <alansyoungiii$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Google-GData

Summary: Handle basic communication with Google services
Name: perl-Net-Google-GData
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Google-GData/

Source: http://www.cpan.org/modules/by-module/Net/Net-Google-GData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Atom)

%description
Handle basic communication with Google services.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Google::Authenticate.3pm*
%doc %{_mandir}/man3/Net::Google::GData.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Google/
#%{perl_vendorlib}/Net/Google/GData/
%{perl_vendorlib}/Net/Google/Authenticate.pm
%{perl_vendorlib}/Net/Google/GData.pm

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
