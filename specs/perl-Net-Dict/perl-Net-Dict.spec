# $Id$
# Authority: dag
# Upstream: Neil Bowers <neil$bowers,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Dict

Summary: Perl module named Net-Dict
Name: perl-Net-Dict
Version: 2.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Dict/

Source: http://www.cpan.org/modules/by-module/Net/Net-Dict-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Dict is a Perl module.

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
%doc ChangeLog MANIFEST README examples/
%doc %{_mandir}/man1/dict.1*
%doc %{_mandir}/man1/tkdict.1*
%doc %{_mandir}/man3/Net::Dict.3pm*
%{_bindir}/dict
%{_bindir}/tkdict
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/Dict/
%{perl_vendorlib}/Net/Dict.pm
%{perl_vendorlib}/Net/Dict.pod

%changelog
* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 2.07-1
- Initial package. (using DAR)
