# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClamAV-Client

Summary: A client class for the ClamAV C<clamd> virus scanner daemon
Name: perl-ClamAV-Client
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClamAV-Client/

Source: http://www.cpan.org/authors/id/J/JM/JMEHNLE/clamav-client/ClamAV-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
A client class for the ClamAV C<clamd> virus scanner daemon.

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
%doc CHANGES MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/ClamAV::Client.3pm*
%doc %{_mandir}/man3/ClamAV::Config.3pm*
%dir %{perl_vendorlib}/ClamAV/
#%{perl_vendorlib}/ClamAV/Client/
%{perl_vendorlib}/ClamAV/Client.pm
%{perl_vendorlib}/ClamAV/Config.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
