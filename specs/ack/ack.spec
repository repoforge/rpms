# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name App-Ack

Summary: Grep-like text search tool
Name: ack
Version: 1.96
Release: 1%{?dist}
License: Artistic
Group: Applications/Text
URL: http://betterthangrep.com/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/ack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::Next) >= 0.40
BuildRequires: perl(Test::More)

%description
ack is a tool like grep, designed for programmers with large trees of
heterogeneous source code. It is written purely in Perl, and takes
advantage of the power of Perl's regular expressions. 

%prep
%setup

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

#check
#{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ack-help.txt ack-help-types.txt Changes META.yml README.markdown TODO
%doc %{_mandir}/man1/ack.1*
%{_bindir}/ack
%dir %{perl_vendorlib}/App/
%{perl_vendorlib}/App/Ack.pm
%{perl_vendorlib}/App/Ack/

%changelog
* Wed May 09 2012 Dag Wieers <dag@wieers.com> - 1.96-1
- Updated to release 1.96.

* Wed Nov 17 2010 Steve Huff <shuff@vecna.org> - 1.94-1
- Update to version 1.94.

* Mon Aug 30 2010 Dag Wieers <dag@wieers.com> - 1.92-1
- Initial package. (using DAR)
