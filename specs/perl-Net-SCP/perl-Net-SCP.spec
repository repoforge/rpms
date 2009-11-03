# $Id$
# Authority: dag
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SCP

Summary: Perl module that implements a secure copy protocol
Name: perl-Net-SCP
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SCP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SCP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Net-SCP is a Perl module that implements a secure copy protocol.

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
%doc Changes MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/Net::SCP.3pm*
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/SCP/
%{perl_vendorlib}/Net/SCP.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
