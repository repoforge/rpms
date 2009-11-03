# $Id$
# Authority: dag
# Upstream: Ian Langworth ? <ian$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-Diff

Summary: Kwiki plugin to display differences between the current wiki page and older revisions
Name: perl-Kwiki-Diff
Version: 0.03
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-Diff/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-Diff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Kwiki plugin to display differences between the current wiki page and older revisions.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Kwiki::Diff.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
#%{perl_vendorlib}/Kwiki/Diff/
%{perl_vendorlib}/Kwiki/Diff.pm

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
