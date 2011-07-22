Name:           ioblazer
Version:        1.01
Release:        3%{?dist}
Group:		Applications/System
Summary:        Multi-platform storage stack micro-benchmark 
License:        MIT
URL:            http://labs.vmware.com/flings/ioblazer
Source0:        http://download3.vmware.com/software/vmw-tools/ioblazer/ioblazer-%{version}.zip 
BuildRequires:	libaio-devel
Requires:	libaio
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
IOBlazer is a multi-platform storage stack micro-benchmark. IOBlazer runs on Linux, Windows and OSX and it is capable of generating a highly customizable workload. 

%prep
%setup -c -q

%build
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0755 ioblazer %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{_bindir}


%changelog
* Wed Apr 20 2011 Sergio Rubio <rubiojr@frameos.org> - 1.01-3
- Fix rpmlint warnings

* Wed Apr 20 2011 Sergio Rubio <rubiojr@frameos.org> - 1.01-2
- re-enable debuginfo

* Tue Apr 19 2011 Sergio Rubio <rubiojr@frameos.org> - 1.01-1
- initial release
