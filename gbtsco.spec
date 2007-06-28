Summary:	gbtsco - Manager that help connection with bluetooth headset
Summary(pl.UTF-8):	gbtsco - Menager pomagający podłączyć zestaw słuchawkowy Bluetooth
Name:		gbtsco
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.stgraber.org/download/projects/gbtsco/%{name}-%{version}.tar.gz
# Source0-md5:	6b802f4e1142cecbb7a0eec0419d99b1
Source1:	%{name}.desktop
Patch0:		%{name}-path_to_glade.patch
URL:		http://www.stgraber.org/category/gbtsco/
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python
Requires:	bluez-hcidump
Requires:	bluez-utils
Requires:	btsco
Requires:	kernel%{_alt_kernel}-char-btsco
Requires:	python-pybluez
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gbtsco is a manager that help connection with bluetooth headset to use
with xmms, audacity or skype. The features of this GUI included the
starting daemon sdpd, hcid and rfcomm and scan MAC address to use with
BTSCO in order to select headphone as sound device.

%description -l pl.UTF-8
gbtsco to menager pomagający przy podłączaniu zestawu słuchawkowego
Bluetooth do używania z XMMS-em, audacity czy skypem. Możliwości
interfejsu graficznego obejmują: uruchomienie demona sdpd, hcid i 
rfcomm oraz skanowanie adresów MAC aby używać ich z BTSCO w celu wyboru
zestawu słuchawkowego jako urządzenia dźwiękowego.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_bindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%attr(755,root,root) %{_datadir}/%{name}/%{name}.glade
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
