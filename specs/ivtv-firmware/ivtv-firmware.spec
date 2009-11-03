# $Id$
# Authority: dag
# Dist: nodist

Summary: Firmware for the Hauppauge PVR 250/350/150/500/USB2 model series
Name: ivtv-firmware
Version: 20070217
Release: 1%{?dist}
License: Redistributable, no modification permitted
Group: System Environment/Kernel
URL: http://dl.ivtvdriver.org/ivtv/firmware/

Source0: http://dl.ivtvdriver.org/ivtv/firmware/firmware-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Obsoletes: ivtv-firmware-audio <= 0.0.1
Provides: ivtv-firmware-audio = 0.0.1
Obsoletes: ivtv-firmware-dec <= 2.02.023
Provides: ivtv-firmware-dec = 2.02.023
Obsoletes: ivtv-firmware-enc <= 2.06.039
Provides: ivtv-firmware-enc = 2.06.039

%description
This package contains the firmware for WinTV Hauppauge PVR
250/350/150/500/USB2cards.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0644 v4l-cx2341x-init.mpg %{buildroot}/lib/firmware/v4l-cx2341x-init.mpg
%{__install} -p -m0644 *.fw %{buildroot}/lib/firmware/

### license requires that the licenses go in the same place as the firmware
for file in license-*.txt; do
    %{__install} -p -m0644 $file %{buildroot}/lib/firmware/ivtv-firmware-$file
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license-*.txt
%dir /lib/firmware/
/lib/firmware/*.fw
/lib/firmware/ivtv-firmware-license-*.txt
/lib/firmware/v4l-cx2341x-init.mpg

%changelog
* Sun Jun 15 2008 Dag Wieers <dag@wieers.com> - 20070217-1
Initial package. (using DAR)
