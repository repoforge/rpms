# $Id: $

# Authority: dries
# Upstream:

Summary: Ultima online server
Name: uox
Version: 0.97.6.9r
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.uox3.org/

Source: http://www.uox3.org/files/uox3-source.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%prep
%setup -c

%build
dos2unix autogen.sh
bash autogen.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc

%changelog
* Fri Apr 30 2004 Dries Verachtert <dries@ulyssis.org> 0.97.6.9r-1
- initial package
