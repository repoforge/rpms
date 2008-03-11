# $Id$
# Authority: dries
# Upstream: Christopher H. Laco <claco$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-NetBlogger

Summary: Catalyst Model to post and retrieve blog entries using Net::Blogger
Name: perl-Catalyst-Model-NetBlogger
Version: 0.04001
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-NetBlogger/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Model-NetBlogger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Catalyst::Runtime) >= 5.33
BuildRequires: perl(ExtUtils::MakeMaker) >= 5.8.0
BuildRequires: perl(Net::Blogger) >= 1.01
Requires: perl >= 2:5.8.0

%description
Catalyst Model to post and retrieve blog entries using Net::Blogger.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo
%doc %{_mandir}/man3/Catalyst::Helper::Model::NetBlogger.3pm*
%doc %{_mandir}/man3/Catalyst::Model::NetBlogger.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Model/
%{perl_vendorlib}/Catalyst/Model/NetBlogger.pm
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Helper/
%dir %{perl_vendorlib}/Catalyst/Helper/Model/
%{perl_vendorlib}/Catalyst/Helper/Model/NetBlogger.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 0.04001-1
- Updated to release 0.04001.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.

