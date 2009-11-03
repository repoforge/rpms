Name: python-forward-compat

%if %{?rh7:1}%{!?rh7:0} || %{?rh9:1}%{!?rh9:0} || %{?fc1:1}%{!?fc1:0}
Version: 2.2
%endif

%if %{?fc2:1}%{!?fc2:0}
Version: 2.3
%endif

Release: 1%{?dist}
Summary: Forward compatibility package for Python %{version}

Group: Development/Languages
License: PSF
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: %{_bindir}/python%{version}
%if ! %{?fc2:1}%{!?fc2:0}
Provides: python-abi = %{version}
%endif
Provides: python(abi) = %{version}

%description
This package provides virtual capabilities and directories for Python
%{version} to make the packaging compatible with newer Python packages.


%prep


%build


%install
%{__rm} -rf %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)


%changelog
* Sun Mar 27 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.x-1
- import into rpmforge
- add python(abi)
- build for py 2.2 and 2.3

* Mon May 31 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2-0.fdr.1
- First build.
