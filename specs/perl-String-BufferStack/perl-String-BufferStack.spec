# $Id$
# Authority: cmr
# Upstream: Alex Vandiver <alexmv$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-BufferStack

Summary: Nested buffers for templating systems
Name: perl-String-BufferStack
Version: 1.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-BufferStack/

Source: http://www.cpan.org/modules/by-module/String/String-BufferStack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
Requires: perl >= 2:5.8.0

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/String::BufferStack.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/BufferStack/
%{perl_vendorlib}/String/BufferStack.pm

%changelog
* Fri Jun 12 2009 Unknown - 1.14-1
- Initial package. (using DAR)
