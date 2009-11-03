# $Id$
# Authority: dag
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Scriptpaths

Summary: Find web relevant paths even without ENV set
Name: perl-CGI-Scriptpaths
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Scriptpaths/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Scriptpaths-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Find web relevant paths even without ENV set.

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
%doc %{_mandir}/man3/CGI::Scriptpaths.3pm*
%dir %{perl_vendorlib}/CGI/
#%{perl_vendorlib}/CGI/Scriptpaths/
%{perl_vendorlib}/CGI/Scriptpaths.pm

%changelog
* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
