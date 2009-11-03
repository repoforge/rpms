# $Id$
# Authority: dag

%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")

Summary: Ruby bindings for RPM
Name: ruby-rpm
Version: 1.2.3
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://rubyforge.org/projects/ruby-rpm/

Source: http://rubyforge.org/frs/download.php/20469/ruby-rpm-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby-devel >= 1.8.1, rpm-devel >= 4.2.1, db4-devel, ruby
Requires: ruby >= 1.8.1

%description
Bindings for accessing RPM packages and databases from Ruby.

%prep
%setup

%build
ruby install.rb config \
	--bin-dir="%{_bindir}" \
	--data-dir="%{_datadir}" \
	--rb-dir="%{ruby_sitelib}" \
	--so-dir="%{ruby_sitearch}"
ruby install.rb setup

%install
%{__rm} -rf %{buildroot}
ruby install.rb config \
	--bin-dir="%{buildroot}%{_bindir}" \
	--data-dir="%{buildroot}%{_datadir}" \
	--rb-dir="%{buildroot}%{ruby_sitelib}" \
	--so-dir="%{buildroot}%{ruby_sitearch}"
ruby install.rb install

%{__chmod} 0755 %{buildroot}%{ruby_sitearch}/rpmmodule.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README doc/
%{ruby_sitearch}/rpmmodule.so
%{ruby_sitelib}/rpm.rb

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Initial package. (using DAR)
