# $Id$
# Authority: dag
# Upstream: Ondřej Vostal <ondra$elfove,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Debug

Summary: Eases the use of debug print with level, indentation and color
Name: perl-Debug
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Debug/

Source: http://www.cpan.org/modules/by-module/Debug/Debug-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Eases the use of debug print with level, indentation and color.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Debug::Message.3pm*
%{perl_vendorlib}/Debug/
#%{perl_vendorlib}/Debug.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
