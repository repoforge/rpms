# $Id$
# Authority: dag
# Upstream: Brian Ingerson <ingy@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Kwiki

Summary: A Quickie Wiki that's not too Tricky
Name: perl-CGI-Kwiki
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Kwiki/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Kwiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
A Quickie Wiki that's not too Tricky.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README ToDo
%doc %{_mandir}/man1/kwiki-install.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/kwiki-install
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Kwiki/
%{perl_vendorlib}/CGI/Kwiki.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
