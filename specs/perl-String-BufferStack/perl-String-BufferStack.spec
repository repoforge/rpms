# $Id$
# Authority: cmr
# Upstream: Alex Vandiver <alexmv$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-BufferStack

Summary: Nested buffers for templating systems
Name: perl-String-BufferStack
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-BufferStack/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/String-BufferStack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl >= 5.8.0
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Nested buffers for templating systems.

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
%doc %{_mandir}/man3/String::BufferStack.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/BufferStack/
%{perl_vendorlib}/String/BufferStack.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Fri Jun 12 2009 Unknown - 1.14-1
- Initial package. (using DAR)
